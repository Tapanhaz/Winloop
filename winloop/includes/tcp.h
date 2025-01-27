#ifndef WINLOOP_TCP_H_
#define WINLOOP_TCP_H_

#pragma once
#include <windef.h>
#include "vendor/include/uv.h"
#include "uv.h"

/* based off of and inspired by src/win/tcp.c 
but with buffers already handled to be very direct... */

/* Turns out there's no other reasonable ways to optimize this down any further
so this is the best I could do - Vizonex */

int try_tcp_write(uv_tcp_t* handle, WSABUF bufs){
  int result;
  DWORD bytes;
 
  if (handle->flags & 0x00000001)
    return UV_EBADF;

  if (handle->stream.conn.write_reqs_pending > 0){
    /* -4088 */
    return UV_EAGAIN;
  }

  result = WSASend(handle->socket, &bufs, 1, &bytes, 0, NULL, NULL);

  if (result == SOCKET_ERROR)  /* FAILED! */
    return uv_translate_sys_error(WSAGetLastError());

  else {
    return bytes;
  }
}

#endif /* TCP_H_ */